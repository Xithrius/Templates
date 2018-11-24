const commando = require('discord.js-commando');
const bot = new Discord.Client();

bot.registry.registerGroup('random', 'Random');
bot.registry.registerCommandsIn(__dirname + "/commands");

bot.login('');
