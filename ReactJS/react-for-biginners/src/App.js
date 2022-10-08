
import {useState, useEffect} from "react";

function App(){
  const [ loading, setLoading ] = useState(true);
  const [ coins, setCoins ] = useState([]);

  const [ dollor, setDollor ] = useState();
  const [ coin, setCoin ] = useState();
  const [ coinsymbol, setCoinSymbol ] = useState();

  const onUsdChange = (event) => {
    setDollor(event.target.value);
  };

  const onCoinChange = (event) => {


  }

  const showValue = (event) => {
    console.log(event);
    console.log(event.target)
    console.log(event.target.value);
  }

  useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers")
    .then((response) => response.json())
    .then((json) => {setCoins(json);
                     setLoading(false)});
    
  }, []);

  console.log(coin, coinsymbol);
  return (
    <div>
      <h1>The Coins! {loading ? "" : `(${coins.length})`}</h1>
      {loading ? <strong>Loading...</strong> : 
      <select onChange={showValue}>
        <option value="none">==Select==</option>
        {coins.map((item) => <option key={item.id}> {item.name}({item.symbol})</option>)}
      </select>}
      
      <div>
        <form>
          <input onChange={onUsdChange} value={dollor} type="text" placeholder="USD" disabled={true} />
          <input onChange={onCoinChange} value={coin} type="text" placeholder={coinsymbol} disabled={true} />

        </form>
      </div>
      
      
    </div>

  );
}

export default App;
