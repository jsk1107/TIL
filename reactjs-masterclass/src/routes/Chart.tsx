import { useQuery } from "react-query";
import { fetchCoinHistory } from "../api/fetchCoin";
import ReactApexChart from "react-apexcharts";
import { useRecoilValue } from "recoil";
import { isDarkAtom } from "../atom";

interface IChartProps {
  coinId: string;
}

interface IHistorycal {
  close: string;
  high: string;
  low: string;
  market_cap: number;
  open: string;
  time_close: number;
  time_open: number;
  volume: string;
}

function Chart({ coinId }: IChartProps) {
  const { isLoading, data } = useQuery<IHistorycal[]>([coinId, "History"], () =>
    fetchCoinHistory(coinId)
  );
  const isDark = useRecoilValue(isDarkAtom);
  return (
    <div>
      {isLoading ? (
        "Loading Chart"
      ) : data ? (
        <ReactApexChart
          type="candlestick"
          series={[
            {
              data: data?.map((price) => ({
                x: price.time_close,
                y: [price.open, price.high, price.low, price.close],
              })),
            },
          ]}
          options={{
            chart: {
              type: "candlestick",
            },
            title: {
              text: "CandleStick Chart",
              align: "left",
            },
            xaxis: {
              type: "datetime",
            },
            yaxis: {
              tooltip: {
                enabled: true,
              },
            },
            theme: { mode: isDark ? "dark" : "light" },
          }}
        />
      ) : (
        "No data"
      )}
    </div>
  );
}

export default Chart;
