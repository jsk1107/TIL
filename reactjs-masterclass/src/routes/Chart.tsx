import { useQuery } from "react-query";
import { fetchCoinHistory } from "../api/fetchCoin";
import ReactApexChart from "react-apexcharts";

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
  return (
    <div>
      {isLoading ? (
        "Loading Chart"
      ) : (
        <ReactApexChart
          type="line"
          series={[
            {
              data: data?.map((price) => parseFloat(price.close)) ?? [],
              name: "sales",
            },
          ]}
          options={{
            chart: { height: 500, width: 500, background: "transparents" },
            theme: { mode: "dark" },
            xaxis: {
              labels: { show: false },
              // type: "datetime",
              categories: data?.map((price) => new Date(price.time_close)),
            },
            yaxis: { show: false },
            grid: { show: false },
            stroke: { curve: "smooth" },
            fill: {
              type: "gradient",
              gradient: { gradientToColors: ["blue"], stops: [0, 100] },
            },
            colors: ["red"],
            tooltip: { y: { formatter: (value) => value.toFixed(3) } },
          }}
        />
      )}
    </div>
  );
}

export default Chart;
