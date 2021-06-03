AVALAIBLE_LEN = ['pt-BR 🇧🇷', 'en-US 🇺🇸']

EN = {
	'greeting' : "Welcome to Vici's Groove, I'm Vici 😘 and here you can let me handle with your musics and set it to a playlist in a simple way 🎧🎵.",
    'menu': {
        'text' : "Por favor, escolha uma das opções para começar",       
        'options': [
            {
                'text': ['Manage playlist'],
                'callback' : ['goPlaylist']
            },
            {
                'text': ['Continue current track'],
                'callback' : ['goSoundtrack']
            },
            {
                'text': ['Manage musics'],
                'callback' : ['goMusics']
            },
            {
                'text': ['Change idiom'],
                'callback' : ['changeLan']
            }]
    }
}

BR = {
	'greeting' : "Bem vindo(a) ao Vici's Groove, meu nome é Vici 😘 e aqui você pode me deixar cuidar de suas músicas e arruma-las em listas de reprodução de uma forma simples🎧🎵.",
    'menu': {
        'text' : "Por favor, escolha uma das opções para começar",       
        'options': [
            {
                'text': ['Gerenciar listas de reprodução'],
                'callback' : ['goPlaylist']
            },
            {
                'text': ['Continuar lista atual'],
                'callback' : ['goSoundtrack']
            },
            {
                'text': ['Gerenciar músicas'],
                'callback' : ['goMusics']
            },
            {
                'text': ['Mudar idioma'],
                'callback' : ['changeLan']
            }]
    }
}