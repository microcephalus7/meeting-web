import React from "react";
import styled from "styled-components";

const SideNav = styled.div`
  width: 100%;
  height: 100vh;
  background-color: black;
`;

const App: React.FC = () => {
  return (
    <>
      <SideNav></SideNav>
    </>
  );
};

export default App;
