define([
    'templates/locales/ca.js',
    'templates/locales/cs.js',
    'templates/locales/de.js',
    'templates/locales/es.js',
    'templates/locales/fr.js',
    'templates/locales/it.js',
    'templates/locales/nl.js',
    'templates/locales/pl.js',
    'templates/locales/pt_br.js',
    'templates/locales/ro.js',
    'templates/locales/ru.js',
    'templates/locales/tr.js',
    'templates/locales/vi.js',
    'templates/locales/zh.js',
    'templates/locales/zh_cn.js'
], function() {
    var langId = (navigator.language || navigator.userLanguage).toLowerCase().replace('-', '_');
    var language = langId.substr(0, 2);
    var locales = {};

    for (index in arguments) {
        for (property in arguments[index])
            locales[property] = arguments[index][property];
    }
    if ( ! locales['en'])
        locales['en'] = {};

    if ( ! locales[langId] && ! locales[language])
        language = 'en';

    var locale = (locales[langId] ? locales[langId] : locales[language]);

    function __(text) {
        var index = locale[text];
        if (index === undefined)
            return text;
        return index;
    };

    function setLanguage(language) {
        locale = locales[language];
    }

    return {
        __         : __,
        locales    : locales,
        locale     : locale,
        setLanguage: setLanguage
    };
});
