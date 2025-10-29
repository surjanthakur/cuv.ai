import './sidebar.css';
import { Sidebar, Plus, MessageSquare } from 'lucide-react';

export default function SidebarWindow() {
  return (
    <>
      <section className="sidebar">
        <Sidebar className="w-5 h-5 text-white" />
        <span>Cuv.ai</span>
        <div>
          <Plus className="w-5 h-5 text-white" />
          <button>New Chat</button>
        </div>
        <MessageSquare />
        <span>Chats</span>
        <div className="recentchats">
          <ul>
            <li>chats</li>
            <li>chats</li>
            <li>chats</li>
            <li>chats</li>
            <li>chats</li>
          </ul>
        </div>
      </section>
    </>
  );
}
