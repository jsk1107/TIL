import styled from "styled-components";

const Container = styled.div`
    
`;

const Header = styled.header``;

const CoinsList = styled.ul``;

const Coin = styled.li``;

const Title = styled.div`
    color: ${props => props.theme.accentColor};
`

const coin = [

]
function Coins() {
    return <Container>
        <Header>
            <Title> 코인 </Title>
        </Header>
        <CoinsList>
            <Coin></Coin>
        </CoinsList>
    </Container>
}

export default Coins;