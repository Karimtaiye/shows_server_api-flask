const input = document.getElementById("input");
const ul = document.getElementById("ul");
input.addEventListener("input", async function (e) {
  // console.log(e.target.value, input.value);
  const response = await fetch(`/search?q=${e.target.value}`);
  const data = await response.json();
  const shows = data.result;

  const elemets = shows.map((el) => {
    return `<li>${el.title}</li>`;
  });
  ul.innerHTML = elemets.join(" ");
  console.log(elemets.join(" "));
});
