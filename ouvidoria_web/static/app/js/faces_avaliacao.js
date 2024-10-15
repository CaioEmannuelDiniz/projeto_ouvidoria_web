const faces = document.querySelectorAll(".face");
const dissatisfactionInput = document.getElementById("dissatisfactionSelected");

faces.forEach((face) => {
  face.addEventListener("click", () => {
    faces.forEach((f) => {
      f.classList.remove("border", "border-blue-500");
    });
    const valor = Array.from(faces).indexOf(face) + 1; // +1 porque o índice começa em 0

    faces[valor - 1].classList.add("border", "border-blue-500");
    dissatisfactionInput.value = valor; // Atualiza o campo oculto com o valor
  });
});
