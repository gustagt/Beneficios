const express = require('express');
const route = express.Router();

const painelCrontroller = require('../src/controllers/painelController');
const consultaController = require("../src/controllers/consultaController");
const formulariosController = require("../src/controllers/formulariosController");

route.get('/', painelCrontroller.paginaInicial);

route.get("/formularioIdoso", painelCrontroller.fIdoso)
route.get("/formularioDeficiente", painelCrontroller.fDeficiente)

route.get("/consulta", consultaController.acompanharProtocolo)
route.post("/consulta", consultaController.pesquisarProtocolo)

route.post("/pedirCredencialIdoso", formulariosController.fIdoso)
route.post("/pedirCredencialDeficiente", formulariosController.fDeficiente)


module.exports = route;

