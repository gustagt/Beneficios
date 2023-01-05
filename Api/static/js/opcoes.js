$('#aprovar').on('click', () =>  {
    opcao = $('#opcao').attr('value', 'aprovado')
})

$('#pendente').on('click', () =>  {
    opcao = $('#opcao').attr('value', 'pendente')
})

$('#indeferir').on('click',() => {
    opcao = $('#opcao').attr('value', 'indeferido')
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
