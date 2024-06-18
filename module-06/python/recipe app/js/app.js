// dom element select
const spinner = document.getElementById("spinner");
const foodList = document.getElementById("food-list");
const searchBtn = document.getElementById("searchBtn");
const searchField = document.getElementById("searchField");
const modalContent = document.getElementById("modal-content");
const scrollToTop = document.getElementById("scrollToTop");

// event listener
window.addEventListener("load", initialLoad);
window.addEventListener("scroll", scrolling);
searchBtn.addEventListener("click", searchFood);
scrollToTop.addEventListener("click", scrollingToTop);

// functionality
async function initialLoad() {
  const apiUrl = `https://www.themealdb.com/api/json/v1/1/search.php?s`;
  const foods = await getData(apiUrl);
  showFood(foods.meals);
}

async function getData(apiUrl) {
  try {
    const res = await fetch(apiUrl);
    const data = await res.json();
    spinner.classList.add("hidden");
    return data;
  } catch (error) {
    console.log(error);
  }
}

function showFood(foods) {
  let foodItem = "";
  foods.forEach((food) => {
    const foodHtml = `
          <div class="food-item">
              <div class="card card-compact bg-base-100 shadow-xl">
                <figure>
                  <img
                    class="w-full h-60 object-cover"
                    src=${food.strMealThumb}
                  />
                </figure>
                <div class="card-body">
                  <h2 class="card-title">${food.strMeal}</h2>
                  <p>
                  ${food.strInstructions.slice(0, 120)}
                  </p>
                  <div class="card-actions justify-end">
                    <label
                      onClick="modal(${food.idMeal})"
                      for="my-modal-6"
                      class="btn btn-warning text-white"
                      >View Details</label
                    >
                  </div>
                </div>
              </div>
            </div>
    `;
    foodItem = foodItem + foodHtml;
  });

  foodList.innerHTML = foodItem;
}

async function searchFood() {
  spinner.classList.remove("hidden");
  foodList.innerHTML = "";
  const searchKeyword = searchField.value;
  const apiUrl = `https://www.themealdb.com/api/json/v1/1/search.php?s=${searchKeyword}`;

  const foods = await getData(apiUrl);

  if (foods.meals === null) {
    return (foodList.innerHTML = "<h2 class=`text-3xl`>No food found</h2>");
  }

  showFood(foods.meals);
}

async function modal(id) {
  modalContent.innerHTML = "";
  const apiUrl = `https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`;
  const food = await getData(apiUrl);

  const html = `
          <div class="card card-compact bg-base-100 shadow-xl">
                    <figure>
                      <img
                        class="w-full h-96 object-cover"
                        src=${food.meals[0].strMealThumb}
                      />
                    </figure>
                    <div class="card-body">
                      <h2 class="card-title">${food.meals[0].strMeal}</h2>
                      <p>
                      ${food.meals[0].strInstructions}
                      </p>
                    </div>
                  </div>
  `;
  modalContent.innerHTML = html;
}

function scrollingToTop() {
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function scrolling() {
  const px = window.pageYOffset;
  if (px > 200) {
    scrollToTop.style.opacity = 1;
    scrollToTop.style.visibility = "visible";
  } else {
    scrollToTop.style.opacity = 0;
    scrollToTop.style.visibility = "hidden";
  }
}
