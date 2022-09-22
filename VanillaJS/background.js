const images = ["0.jpeg", "1.png", "2.png"]

// Math.random: 0~1 사이의 임의의 값을 출력.
// 여기에 images의 길이를 곱해주고 내림처리를 해주면 images 배열길이만큼의 Index를 랜덤한 값을 얻을 수 있다.
const randomNumber = Math.floor(Math.random() * images.length)

const imgSection = document.createElement("img");
imgSection.src = images[randomNumber]
imgSection.setAttribute("width", "800px") // setAttribute: 생성된 태그(노드)에 속성을 부여한다.

console.log(imgSection, randomNumber);

// document.body.appendChild는 body부분에 tag를 추가한다(맨마지막에 추가됨).
document.body.appendChild(imgSection);