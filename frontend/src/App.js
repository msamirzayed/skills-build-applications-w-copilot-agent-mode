import React from 'react';
import Dashboard from './components/Dashboard';
import ActivityLog from './components/ActivityLog';
import Leaderboard from './components/Leaderboard';
import TeamManagement from './components/TeamManagement';
import UserProfile from './components/UserProfile';

function App() {
  return (
    <div>
      <h1>OctoFit Tracker</h1>
      <Dashboard />
      <ActivityLog />
      <Leaderboard />
      <TeamManagement />
      <UserProfile />
    </div>
  );
}

export default App;
