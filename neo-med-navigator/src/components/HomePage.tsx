import { useState } from 'react';
import DataUploadSection from './DataUploadSection';
import DrugRecommendationsSection from './DrugRecommendationsSection';

const HomePage = () => {
  const [recommendations, setRecommendations] = useState([]);

  return (
    <>
      <DataUploadSection setRecommendations={setRecommendations} />
      <DrugRecommendationsSection recommendations={recommendations} />
    </>
  );
};

export default HomePage;
