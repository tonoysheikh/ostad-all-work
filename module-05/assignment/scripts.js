let count = 199;
let roomnum = 1;
let count1 = 249;
let roomnum1 = 1;

const priceTag = document.getElementById("price");
const roomamt = document.getElementById("room");
const button1 = document.getElementById("button1");
const button2 = document.getElementById("button2");
const roombook = document.getElementById("finalroom");

button1.addEventListener("click", () => {
  count += 199;
  roomnum++;
  priceTag.textContent = `$${count}`;
  roomamt.textContent = `${roomnum} room`;
  roombook.textContent = `Thanks for choosing ${roomnum} room`;
});

button2.addEventListener("click", () => {
  if (count > 199) {
    count -= 199;
    roomnum--;
  }
  priceTag.textContent = `$${count}`;
  roomamt.textContent = `${roomnum} room`;
  roombook.textContent = `Thanks for choosing ${roomnum} room`;

});

const priceTag1 = document.getElementById("price1");
const roomamt1 = document.getElementById("room1");
const button3 = document.getElementById("button3");
const button4 = document.getElementById("button4");

button3.addEventListener("click", () => {
  count1 += 249;
  roomnum1++;
  priceTag1.textContent = `$${count1}`;
  roomamt1.textContent = `${roomnum1} room`;
});

button4.addEventListener("click", () => {
  if (count1 > 249) {
    count1 -= 249;
    roomnum1--;
  }
  priceTag1.textContent = `$${count1}`;
  roomamt1.textContent = `${roomnum1} room`;
});
