
var linhasPagina = 13;

var tabela = document.getElementById("minhaTabela");

var totalLinhas = tabela.rows.length;

var totalPaginas = Math.ceil(totalLinhas / linhasPagina);
// tela_impressao = window.open('about:blank');

// tela_impressao.document.write(table.outerHTML)
// tela_impressao.window.print()




for (var i = 1; i <= totalPaginas; i++) {
  if (i > 10) {
    break;
  }
  criarBotao(i, 1);
}

eventoBotao();

showPage(1, '1');

$(".rows").click(
  function (e) {

      var valorCelula = this.cells[0].textContent

      document.cookie = "numero="+valorCelula+"; path=/";

      $('form[name="formulario"]').submit()
  }
)

$(document).ready(function() {
  $("#barraPesquisa").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#corpoTabela tr").filter(function() {
          if (value == ""){
            document.location.reload()
          }

          $(this).toggle($(this).text()
          .toLowerCase().indexOf(value) > -1)
      });
  });
});

function showPage(page, id) {


  for (var i = 0; i < totalLinhas; i++) {
    tabela.rows[i].style.display = "none";
  }


  var startIndex = ((page - 1) * linhasPagina) + 1;
  var endIndex
  if (startIndex > (totalLinhas - 14)) {
    endIndex = totalLinhas - 1;
  } else {
    endIndex = startIndex + linhasPagina - 1;
  }

  tabela.rows[0].style.display = "table-row";
  for (var i = startIndex; i <= endIndex; i++) {
    tabela.rows[i].style.display = "table-row";
  }

  var activePage = document.getElementsByClassName("active")[0];
  activePage.classList.remove("active");
  botao = document.getElementById(id)
  botao.classList.add("active");


  paginacao(page);
}

function paginacao(page) {
  if (page > 6) {
    $('.page').remove();
    for (var i = (page - 5); i <= (parseInt(page) + 4); i++) {
      if (i > totalPaginas) {
        break;
      }
      criarBotao(i, page);
    }

    eventoBotao();
  } else {
    $('.page').remove();
    for (var i = 1; i <= totalPaginas; i++) {
      if (i > 10) {
        break;
      }

      criarBotao(i, page)
    }
    eventoBotao();


  }
}

function criarBotao(i, page) {
  var button = document.createElement("a");
  button.innerHTML = i;
  button.href = "#";
  button.classList.add("page");
  button.id = i;

  if (i == page) {
    button.classList.add("active");
  }

  document.getElementById("pagination").appendChild(button);
}

function eventoBotao() {
  var pages = document.getElementsByClassName("page");
  for (var i = 0; i < pages.length; i++) {
    pages[i].addEventListener("click", function () {
      
      var currentPage = this.innerHTML;
      showPage(currentPage, this.id);
    });
  }
}

