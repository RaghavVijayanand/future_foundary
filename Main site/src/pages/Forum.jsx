import React from 'react';
import { motion } from 'framer-motion';
import { MessageCircle, ThumbsUp, Reply, Plus } from 'lucide-react';

const Forum = () => {
  const forumPosts = [
    {
      id: 1,
      title: 'How to transition from Engineering to Data Science?',
      author: 'Alex Johnson',
      time: '2 hours ago',
      replies: 12,
      likes: 25,
      category: 'Career Transition',
      excerpt: 'I have been working as a software engineer for 3 years and want to move into data science...',
    },
    {
      id: 2,
      title: 'Best programming languages for beginners in 2024',
      author: 'Sarah Miller',
      time: '5 hours ago',
      replies: 8,
      likes: 18,
      category: 'Programming',
      excerpt: 'Starting my programming journey and confused about which language to pick first...',
    },
    {
      id: 3,
      title: 'Remote work vs Office: What are your experiences?',
      author: 'Mike Chen',
      time: '1 day ago',
      replies: 24,
      likes: 42,
      category: 'Work Culture',
      excerpt: 'Been working remotely for 2 years now and considering switching back to office...',
    },
  ];

  const categories = [
    'All Topics',
    'Career Transition',
    'Programming',
    'Work Culture',
    'Skill Development',
    'Interview Tips',
    'Freelancing',
    'Entrepreneurship',
  ];

  return (
    <div className="forum">
      <div className="container">
        <motion.div
          className="page-header"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <MessageCircle size={40} className="page-icon" />
          <h1>Community Forum</h1>
          <p>Connect with professionals, share experiences, and get advice from the community</p>
        </motion.div>

        <div className="forum-layout">
          <div className="forum-sidebar">
            <button className="btn btn-primary new-post-btn">
              <Plus size={20} />
              New Post
            </button>
            
            <div className="categories-section">
              <h3>Categories</h3>
              <ul className="categories-list">
                {categories.map((category, index) => (
                  <li key={index} className={`category-item ${index === 0 ? 'active' : ''}`}>
                    {category}
                  </li>
                ))}
              </ul>
            </div>
          </div>

          <div className="forum-main">
            <div className="forum-header">
              <h2>Latest Discussions</h2>
              <select className="sort-select">
                <option>Latest</option>
                <option>Most Popular</option>
                <option>Most Replies</option>
              </select>
            </div>

            <div className="posts-list">
              {forumPosts.map((post, index) => (
                <motion.div
                  key={post.id}
                  className="post-card card"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                >
                  <div className="post-header">
                    <div className="post-meta">
                      <span className="category-tag">{post.category}</span>
                      <span className="post-time">{post.time}</span>
                    </div>
                  </div>
                  
                  <h3 className="post-title">{post.title}</h3>
                  <p className="post-excerpt">{post.excerpt}</p>
                  
                  <div className="post-footer">
                    <div className="post-author">
                      By <strong>{post.author}</strong>
                    </div>
                    <div className="post-stats">
                      <span className="stat">
                        <ThumbsUp size={16} />
                        {post.likes}
                      </span>
                      <span className="stat">
                        <Reply size={16} />
                        {post.replies}
                      </span>
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Forum;
