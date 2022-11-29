exports.paginaInicial = (req, res) => {
    res.render('index');
};

exports.fIdoso = (req, res) => {
    res.render('fCredencialIdoso');
};

exports.fDeficiente = (req, res) => {
    res.render('fCredencialDeficiente');
};
