
import {useState, useEffect} from "react";

function App(){
  const [ loading, setLoading] = useState(true);
  const [coins, setCoins] = useState([]);

  useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers")
    .then((response) => response.json())
    .then((json) => {setCoins(json);
                     setLoading(false)});
    
  }, []);

  return (
    <div>
      <h1>The Coins!</h1>
      {loading ? <strong>Loading...</strong> : 
      <select>
        {coins.map((item) => <option key={item.id}> {item.name} {item.symbol} ${item.quotes.USD.price}</option>)}
      </select>}
      
    </div>

  );
}

export default App;
