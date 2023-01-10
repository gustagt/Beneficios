$('#aprovar').on('click', () =>  {
    opcao = $('#opcao').attr('value', 'aprovado')    
    var data = document.getElementById("dataValidade")
    var tipoDef = document.getElementById("tipoDeficiencia")
    data.required = true
    tipoDef.required = true
})

$('#pendente').on('click', () =>  {
    opcao = $('#opcao').attr('value', 'pendente')
    var data = document.getElementById("dataValidade")
    var tipoDef = document.getElementById("tipoDeficiencia")
    data.required = false
    tipoDef.required = false
})

$('#indeferir').on('click',() => {
    opcao = $('#opcao').attr('value', 'indeferir')
    var data = document.getElementById("dataValidade")
    var tipoDef = document.getElementById("tipoDeficiencia")
    data.required = false
    tipoDef.required = false
})

$('#credencial').on('click',() => {
    opcao = $('#formulario').attr('action', '/opcoes/credencial')
    opcao = $('#formulario').attr('method', 'get')
})

$('#credencialPt').on('click',() => {
    opcao = $('#formulario').attr('action', '/opcoes/protocolo/credencial')
    opcao = $('#formulario').attr('method', 'get')
})

$('#salvarAR').on('click',() => {
    opcao = $('#formulario').attr('action', '/opcoes/salvarAR')
    opcao = $('#formulario').attr('method', 'post')
})

$('#confirmarEntrega').on('click',() => {
    opcao = $('#formulario').attr('action', '/opcoes/anexarAR')
    opcao = $('#formulario').attr('enctype', 'multipart/form-data')
})

var button = document.getElementById("salvarAR")

$('#ar').on('keyup', () => {
    if ($('#ar').val() === "") {
        // Se estive vazio, desativa o botão
        button.disabled = true;
    } else {
        // Se não estiver vazio, ativa o botão
        button.disabled = false;
    }
})

var button2 = document.getElementById("confirmarEntrega")

$('#arFile').on('change', () => {
    if ($('#arFile').files == 0) {
        // Se estive vazio, desativa o botão
        button2.disabled = true;
    } else {
        // Se não estiver vazio, ativa o botão
        button2.disabled = false;
    }
})


// documentos
$('#dcOfFoto').on('click', () =>  {
    window.location.href = "/documentos/oficial_foto"
})

$('#laudoPericial').on('click', () =>  {
    window.location.href = "/documentos/laudo_perificial"
})

$('#cpResidencia').on('click',() => {
    window.location.href = "/documentos/comprovante_residencia"
})

$('#dResponsavel').on('click',() => {
    window.location.href = "/documentos/representante_legal"
})

$('#docAR').on('click',() => {
    window.location.href = "/documentos/AR"
})
