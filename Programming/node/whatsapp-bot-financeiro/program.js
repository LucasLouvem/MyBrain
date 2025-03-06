const makeWASocket = require('@whiskeysockets/baileys').default;
const { default: makeWASocket, useSingleFileAuthState } = require('@whiskeysockets/baileys');
const fs = require('fs');
const path = require('path');
const sqlite3 = require('better-sqlite3');
const { Boom } = require('@hapi/boom');

// Configurar banco de dados
const db = new sqlite3('./gastos.db');
db.prepare(`CREATE TABLE IF NOT EXISTS gastos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor REAL,
    descricao TEXT,
    tipo TEXT,
    data TEXT
)`).run();

async function startBot() {
    // Inicializa autenticação corretamente
    const { state, saveState } = await useSingleFileAuthState('./auth_info.json');
    
    const sock = makeWASocket({ auth: state });
    sock.ev.on('creds.update', saveState);
    
    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect } = update;
        if (connection === 'close') {
            const shouldReconnect = lastDisconnect?.error?.output?.statusCode !== 401;
            console.log('Conexão perdida. Reconectando...', shouldReconnect);
            if (shouldReconnect) startBot();
        } else if (connection === 'open') {
            console.log('Bot conectado ao WhatsApp!');
        }
    });

    sock.ev.on('messages.upsert', async (msg) => {
        const message = msg.messages[0];
        if (!message.message || message.key.fromMe) return;
        
        const from = message.key.remoteJid;
        const text = message.message.conversation || '';
        
        if (text.toLowerCase() === 'total') {
            const { credito, debito } = calcularTotal();
            await sock.sendMessage(from, { text: `📊 Total gasto este mês:\n💳 Crédito: R$${credito.toFixed(2)}\n🏦 Débito: R$${debito.toFixed(2)}` });
        } else if (/^r?\$?\d+/i.test(text)) {
            registrarGasto(text);
            await sock.sendMessage(from, { text: '✅ Gasto registrado!' });
        }
    });
}

function registrarGasto(texto) {
    const regex = /R?\$?(\d+(?:\.\d+)?)\s*-\s*(.+?)\s*\((crédito|débito)\)/i;
    const match = texto.match(regex);
    if (!match) return;
    
    const valor = parseFloat(match[1]);
    const descricao = match[2];
    const tipo = match[3].toLowerCase();
    const data = new Date().toISOString().split('T')[0];
    
    db.prepare('INSERT INTO gastos (valor, descricao, tipo, data) VALUES (?, ?, ?, ?)')
        .run(valor, descricao, tipo, data);
}

function calcularTotal() {
    const mesAtual = new Date().toISOString().slice(0, 7);
    const query = db.prepare(`SELECT SUM(valor) as total, tipo FROM gastos WHERE data LIKE ? GROUP BY tipo`);
    const rows = query.all(`${mesAtual}%`);
    
    let credito = 0, debito = 0;
    rows.forEach(row => {
        if (row.tipo === 'crédito') credito = row.total;
        else if (row.tipo === 'débito') debito = row.total;
    });
    return { credito, debito };
}

// Chamando a função corretamente
startBot();

