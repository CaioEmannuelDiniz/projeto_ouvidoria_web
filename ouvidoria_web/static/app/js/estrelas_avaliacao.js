const stars = document.querySelectorAll(".star");
const satisfactionInput = document.getElementById("satisfactionSelected");


stars.forEach((star) => {
  star.addEventListener("click", () => {
    stars.forEach((s) => {
      s.classList.remove("text-yellow-500");
      s.classList.add("text-gray-300");
    });
    const valor = Array.from(stars).indexOf(star) + 1; // +1 porque o índice começa em 0
    for (let i = 0; i < valor; i++) {
      stars[i].classList.add("text-yellow-500");
    }
    satisfactionInput.value = valor; // Atualiza o campo oculto com o valor
  });
});
