import React from "react";
import styled from "styled-components";

const Wrapper = styled.div`
  width: 100%;
  height: 100vh;
  display: flex;
`;
const SideNav = styled.div`
  width: 400px;
  border: black 1px solid;
`;
const Main = styled.div`
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
`;
const Recom = styled.div`
  width: 350px;
  height: 600px;
  border: black 1px solid;
  display: flex;
  flex-direction: column;
`;
const Profile = styled.div`
  width: 100%;
  height: 80%;
  border: black 1px solid;
`;
const Actions = styled.div`
  width: 100%;
  height: 20%;
`;

const App: React.FC = () => {
  return (
    <Wrapper>
      <SideNav></SideNav>
      <Main>
        <Recom>
          <Profile></Profile>
          <Actions></Actions>
        </Recom>
      </Main>
    </Wrapper>
  );
};

export default App;
