// Variáveis
let valor = 0;
let fechar;
let toast;
let mensagem;
let tipo;
let barraProgresso;

update();

// Função para atualizar os elementos DOM
function update() {
  fechar = document.getElementById("close");
  toast = document.getElementById("toast");
  mensagem = document.getElementById("message");
  tipo = document.getElementById("type");
  barraProgresso = document.getElementById("progress");
}

// Eventos
fechar.addEventListener("click", fecharToast);

// Funções
const carregamento = setInterval(() => {
  valor += 1;

  if (valor === 100) {
    setTimeout(() => {
      fecharToast();
    }, 200);

    clearInterval(carregamento);
  }
  barraProgresso.style.width = `${valor}%`;
}, 60);

function fecharToast() {
  toast.classList.remove("toast");
  toast.classList.add("hidden");
  valor = 0;
}

function showToast(tipoToast, texto) {
  // Atualiza os elementos antes de usar
  update();

  toast.classList.remove("hidden");

  toast.classList.add("toast");

  switch (tipoToast) {
    case "error":
      tipo.classList.add("border-red-500");
      tipo.classList.add("bg-red-500");
      tipo.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg"
        class="w-10 h-10 text-white"  
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round">
        <path d="M18 6L6 18M6 6l12 12" />
        </svg>`;
      mensagem.innerText = texto;
      barraProgresso.classList.add("bg-red-500");
      break;
    case "sucess":
      tipo.classList.add("border-green-500");
      tipo.classList.add("bg-green-500");
      tipo.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg"
        class="w-10 h-10 mr-2 text-white"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round">
        <path d="M9 11l3 3L22 4" />
      </svg>`;
      mensagem.innerText = texto;
      barraProgresso.classList.add("bg-green-500");
      break;
    case "warning":
      tipo.classList.add("border-yellow-500");
      tipo.classList.add("bg-yellow-500");
      tipo.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg"
        class="w-10 h-10 text-white"  
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round">
        <path d="M12 2v8M12 18h0" />
        </svg>`;
      mensagem.innerText = texto;
      barraProgresso.classList.add("bg-yellow-500");
      break;
    case "info":
      tipo.classList.add("border-blue-500");
      tipo.classList.add("bg-blue-500");
      tipo.innerHTML = `<svg class="w-10 h-10 text-white" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <circle cx="12" cy="12" r="10" fill="none"/>
      <path d="M12 8v4M12 16h0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
      </svg>`;
      mensagem.innerText = texto;
      barraProgresso.classList.add("bg-blue-500");
      break;
  }
}
