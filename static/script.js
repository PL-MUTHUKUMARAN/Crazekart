/* ------------------- CATEGORY MENU ------------------- */
const categoriesIcon = document.getElementById("categories-icon");
const categories = document.querySelector(".categories");
const productsContainer = document.querySelector(".products-container");

if (categoriesIcon) {
  categoriesIcon.addEventListener("click", (e) => {
    e.stopPropagation();
    categories.classList.toggle("show");
    productsContainer.classList.toggle("add");
  });
}

const profileIcon = document.querySelector(".profile-icon");
const dropdownMenu = document.getElementById("dropdown-menu");

if (profileIcon) {
  profileIcon.addEventListener("click", (e) => {
    e.stopPropagation();
    dropdownMenu.classList.toggle("show");
  });

  document.addEventListener("click", () => {
    dropdownMenu.classList.remove("show");
  });
}

/* ------------------- SEARCH BOX ------------------- */
const searchIcon = document.getElementById("search-icon");
const searchBoxContainer = document.querySelector(".search-box-container");
const searchBox = document.querySelector(".search-box");
const searchClose = document.getElementById("search-close");

if (searchIcon) {
  searchIcon.addEventListener("click", (e) => {
    e.stopPropagation();
    searchBoxContainer.classList.toggle("active");
    searchBox.focus();
  });

  searchClose.addEventListener("click", (e) => {
    e.stopPropagation();
    searchBoxContainer.classList.remove("active");
    searchBox.value = "";
  });

  document.addEventListener("click", (e) => {
    if (!searchBoxContainer.contains(e.target)) {
      searchBoxContainer.classList.remove("active");
    }
  });
}

/* ------------------- SEARCH FUNCTIONALITY ------------------- */
const searchInput = document.getElementById("searchInput");

searchInput.addEventListener("input", function () {
  const query = this.value.toLowerCase();
  const productCards = document.querySelectorAll(".products-card");

  productCards.forEach((card) => {
    const name = card.querySelector(".product-title").textContent.toLowerCase();
    card.style.display = name.includes(query) ? "block" : "none";
  });
});

/* ------------------- BRAND FILTER ------------------- */
const checkboxes = document.querySelectorAll(".brand-checkbox");
const productCards = document.querySelectorAll(".products-card");

checkboxes.forEach((checkbox) => {
  checkbox.addEventListener("change", () => {
    const selectedBrands = Array.from(checkboxes)
      .filter((cb) => cb.checked)
      .map((cb) => cb.value);

    productCards.forEach((card) => {
      const cardBrand = card.dataset.brand;
      card.style.display =
        selectedBrands.length === 0 || selectedBrands.includes(cardBrand)
          ? "block"
          : "none";
    });
  });
});

/* ------------------- IMAGE SWITCHING ------------------- */
const buyButton = document.querySelectorAll(".buy-button");

buyButton.forEach((button) => {
  button.addEventListener("click", () => {
    const productId = button.dataset.id;

    const productDetails = {
      color: button.dataset.color || "",
      vcolor: button.dataset.vcolor || "",
      image: button.dataset.image || "",
    };

    localStorage.setItem("productDetails", JSON.stringify(productDetails));

    window.location.href = `/buyingProductDetails/${productId}`;
  });
});

const product = JSON.parse(localStorage.getItem("productDetails"));

const selectedProduct = product.image;
const color = document.querySelector(".color");
if (color) {
  color.innerText = product.color;
}

const buyingProductImages = document.querySelectorAll(".product-image");
const mainProductImage = document.querySelector(".main-product-image");
const productColor1 = document.querySelector(".productColor1");
const productColor2 = document.querySelector(".productColor2");
const cartImage = document.getElementById("cart-image");
const buyImage = document.getElementById("buy-image");

if (selectedProduct && buyingProductImages.length > 0) {
  buyingProductImages.forEach((img, index) => {
    img.src = `${STATIC_URL}assets/products/${selectedProduct}${index + 1}.webp`;
  });

  if (mainProductImage)
    mainProductImage.src = `${STATIC_URL}assets/products/${selectedProduct}1.webp`;

  if (productColor1)
    productColor1.src = `${STATIC_URL}assets/products/${selectedProduct}1.webp`;

  if (productColor2)
    productColor2.src = `${STATIC_URL}assets/products/${selectedProduct}11.webp`;

  if (cartImage && buyImage && product) {
    cartImage.value = `${product.image}1`;
    buyImage.value = `${product.image}1`;
  }
}

buyingProductImages.forEach((img, index) => {
  img.addEventListener("click", () => {
    if (mainProductImage) mainProductImage.src = img.src;
    stopImageSlide();
    showProductImage(index);
    startImageSlide();
  });
});

if (productColor2) {
  productColor2.addEventListener("click", () => {
    buyingProductImages.forEach((img, index) => {
      img.src = `${STATIC_URL}assets/products/${selectedProduct}${index + 1}1.webp`;
    });
    mainProductImage.src = `${STATIC_URL}assets/products/${selectedProduct}11.webp`;
    if (color) {
      color.innerText = product.vcolor;
    }
    if (cartImage && buyImage && product) {
      cartImage.value = `${product.image}11`;
      buyImage.value = `${product.image}11`;
    }
    stopImageSlide();
    startImageSlide();
  });
}

if (productColor1) {
  productColor1.addEventListener("click", () => {
    buyingProductImages.forEach((img, index) => {
      img.src = `${STATIC_URL}assets/products/${selectedProduct}${index + 1}.webp`;
    });
    mainProductImage.src = `${STATIC_URL}assets/products/${selectedProduct}1.webp`;
    if (color) {
      color.innerText = product.color;
    }
    if (cartImage && buyImage && product) {
      cartImage.value = `${product.image}1`;
      buyImage.value = `${product.image}1`;
    }
    stopImageSlide();
    startImageSlide();
  });
}

/* ------------------- PRODUCT MAIN IMAGE SLIDER ------------------- */
let currentIdx = 0;
let autoProductSlide;
const prevButton = document.querySelector(".prod-prev");
const nextButton = document.querySelector(".prod-next");

function showProductImage(index) {
  if (index >= buyingProductImages.length) index = 0;
  if (index < 0) index = buyingProductImages.length - 1;
  if (mainProductImage) mainProductImage.src = buyingProductImages[index].src;
  currentIdx = index;
}

function nextImage() {
  showProductImage(currentIdx + 1);
}

function prevImage() {
  showProductImage(currentIdx - 1);
}

function startImageSlide() {
  autoProductSlide = setInterval(nextImage, 3000);
}

function stopImageSlide() {
  clearInterval(autoProductSlide);
}

if (prevButton) {
  prevButton.addEventListener("click", () => {
    prevImage();
    stopImageSlide();
    startImageSlide();
  });
}

if (nextButton) {
  nextButton.addEventListener("click", () => {
    nextImage();
    stopImageSlide();
    startImageSlide();
  });
}

startImageSlide();

/* ------------------- COLOR VARY ------------------- */
document.querySelectorAll("form").forEach((form) => {
  form.addEventListener("submit", () => {
    const selectedColor = document.querySelector(".color")?.innerText.trim() || "";
    const input = form.querySelector("input[name='color']");
    if (input) input.value = selectedColor;
  });
});

/* ------------------- BANNER SLIDER ------------------- */
const slides = document.querySelectorAll(".banners-wrapper .banner");
const prevBtn = document.querySelector(".prev");
const nextBtn = document.querySelector(".next");
const bannersWrapper = document.querySelector(".banners-wrapper");
const dotsContainer = document.querySelector(".dots-container");

let currentIndex = 0;
let autoSlideInterval;
let dots = [];

function showSlide(index) {
  if (slides.length === 0) return;
  if (index < 0) index = slides.length - 1;
  if (index >= slides.length) index = 0;

  const slidePercent = 100 / slides.length;
  bannersWrapper.style.transform = `translateX(-${index * slidePercent}%)`;

  dots.forEach((d) => d.classList.remove("active"));
  if (dots[index]) dots[index].classList.add("active");

  currentIndex = index;
}

function nextSlide() {
  showSlide(currentIndex + 1);
}

function prevSlide() {
  showSlide(currentIndex - 1);
}

function goToSlide(index) {
  showSlide(index);
}

function startAutoSlide() {
  autoSlideInterval = setInterval(nextSlide, 3000);
}

function stopAutoSlide() {
  clearInterval(autoSlideInterval);
}

if (slides.length > 0) {
  slides.forEach((_, index) => {
    const dot = document.createElement("span");
    dot.classList.add("dot");
    if (index === 0) dot.classList.add("active");
    dot.addEventListener("click", () => {
      stopAutoSlide();
      goToSlide(index);
      startAutoSlide();
    });
    dotsContainer.appendChild(dot);
    dots.push(dot);
  });

  if (prevBtn) {
    prevBtn.addEventListener("click", () => {
      stopAutoSlide();
      prevSlide();
      startAutoSlide();
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener("click", () => {
      stopAutoSlide();
      nextSlide();
      startAutoSlide();
    });
  }

  showSlide(currentIndex);
  startAutoSlide();
}

/* ------------------- RESPONSIVE BANNER IMAGE ------------------- */
function updateImage() {
  const images = document.querySelectorAll(".banner img");
  images.forEach((img, index) => {
    img.src =
      window.innerWidth <= 720
        ? `${STATIC_URL}assets/banner/img${index + 1}_mobile.jpg`
        : `${STATIC_URL}assets/banner/img${index + 1}.jpg`;
  });
}

updateImage();
window.addEventListener("resize", updateImage);
