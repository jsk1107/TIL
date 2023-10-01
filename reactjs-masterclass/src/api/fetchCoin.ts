export default function fetchCoin() {
  return fetch("https://api.coinpaprika.com/v1/tickers").then((res) =>
    res.json()
  );
}
