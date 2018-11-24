const Discord = require('discord.js');
const bot = new Discord.Client();

bot.on('message', (message) => {

  if (message.content == 'ping') {
    // message.reply('pong'); or
    message.channel.send('pong');
  }

});

bot.login('NDg1MDA5NTIzNTM1MjQ5NDA4.Dtoo_A.A1uM-wJSLXwbKIjw_R3tjny4TVQ');
