import { useParams } from "react-router-dom";

interface ICoin {
    coinId: string;
}

function Coin() {
    // url의 queryString을 가지고온다. 
    // key는 Route에서 :coinId 이런식으로 쓰면 coinId가 key가 된다. value는 사용자가 입력한 값
    const { coinId } = useParams<ICoin>();

    console.log(coinId);
    return (
        <div> coinId: {coinId}</div>
    )
}

export default Coin;