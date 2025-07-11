// Wait for the DOM to be ready
document.addEventListener("DOMContentLoaded", function () {
  // Variable Declarations
  const slides = document.getElementsByClassName("items");
  let currentSlide = 0;
  let autoSwap = setInterval(swap, 3500); // Automatic slideshow interval

  // Collect slide items and initialize variables
  const items = Array.from(document.querySelectorAll(".carousel li.items"));
  const itemCount = items.length;
  let startItem = 1;
  let position = 0;

  // Function to handle slideshow rotation
  function swap(action) {
    const direction =
      action === "counter-clockwise" ? "counter-clockwise" : "clockwise";

    // Helper function to determine new position based on direction
    function calculatePosition(direction) {
      position = direction === "counter-clockwise" ? itemCount - 1 : 1;
      return position;
    }

    // Swap slide classes based on direction
    if (direction === "counter-clockwise") {
      items[
        (startItem + calculatePosition(direction) - 1) % itemCount
      ].classList.remove("main-pos");
      items[
        (startItem + calculatePosition(direction)) % itemCount
      ].classList.remove("right-pos");
      items[
        (startItem + calculatePosition(direction)) % itemCount
      ].classList.add("main-pos");
      items[
        (startItem + calculatePosition(direction) + 1) % itemCount
      ].classList.remove("left-pos");
      items[
        (startItem + calculatePosition(direction) - 1) % itemCount
      ].classList.add("left-pos");
      startItem--;
      if (startItem < 1) {
        startItem = itemCount;
      }
    } else {
      items[(startItem - 1) % itemCount].classList.remove("main-pos");
      items[
        (startItem + calculatePosition(direction)) % itemCount
      ].classList.add("main-pos");
      items[
        (startItem + calculatePosition(direction)) % itemCount
      ].classList.remove("right-pos");
      items[
        (startItem + calculatePosition(direction) + 1) % itemCount
      ].classList.add("right-pos");
      items[(startItem - 1) % itemCount].classList.remove("left-pos");
      items[
        (startItem + calculatePosition(direction) - 1) % itemCount
      ].classList.add("left-pos");
      startItem++;
      if (startItem > itemCount) {
        startItem = 1;
      }
    }
  }

  // Function to handle slide transition when arrow buttons are clicked
  document.getElementById("prev").addEventListener("click", () => {
    clearInterval(autoSwap); // Stop the automatic slideshow
    swap("counter-clockwise"); // Move to the previous slide
  });

  document.getElementById("next").addEventListener("click", () => {
    clearInterval(autoSwap); // Stop the automatic slideshow
    swap("clockwise"); // Move to the next slide
  });

  // Event listener for clicking on slides to change rotation direction
  document.querySelectorAll("li.items").forEach((item) => {
    item.addEventListener("click", () => {
      clearInterval(autoSwap); // Stop the automatic slideshow
      if (item.classList.contains("left-pos")) {
        swap("counter-clockwise"); // Move to the previous slide
      } else {
        swap("clockwise"); // Move to the next slide
      }
    });
  });
});
