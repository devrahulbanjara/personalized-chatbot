import React, { useState, useRef, useEffect } from 'react';
import { MessageSquare, Send, X, User, Bot, Mic } from 'lucide-react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

const Index = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const {
    transcript,
    listening,
    resetTranscript,
    browserSupportsSpeechRecognition
  } = useSpeechRecognition();

  useEffect(() => {
    if (transcript) {
      setInputValue(transcript);
    }
  }, [transcript]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage: Message = { role: 'user', content: inputValue };
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);
    resetTranscript();

    try {
      const response = await fetch('http://127.0.0.1:8000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: inputValue }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const assistantMessage: Message = {
        role: 'assistant',
        content: data.response || 'No response from the bot.'
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      const errorMessage: Message = {
        role: 'assistant',
        content: `Error: ${error instanceof Error ? error.message : 'Unknown error occurred'}`
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const handleListen = () => {
    if (listening) {
      SpeechRecognition.stopListening();
    } else {
      resetTranscript();
      SpeechRecognition.startListening({ continuous: false });
    }
  };

  if (!browserSupportsSpeechRecognition) {
    console.log("Browser doesn't support speech recognition.");
    // You could render a fallback or disable the mic button here
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 relative overflow-hidden">
      {/* Background decorative elements */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute -top-4 -right-4 w-96 h-96 bg-blue-100/30 rounded-full blur-3xl"></div>
        <div className="absolute -bottom-4 -left-4 w-96 h-96 bg-purple-100/30 rounded-full blur-3xl"></div>
      </div>

      {/* Main content */}
      <div className="relative z-10 flex items-center justify-center min-h-screen p-8">
        <div className="text-center max-w-3xl">
          <h1 className="text-7xl font-extrabold text-slate-800 mb-6 animate-fade-in-down bg-gradient-to-r from-blue-600 to-purple-700 bg-clip-text text-transparent">
            Rahul Dev Banjara Chatbot
          </h1>
          <p className="text-2xl text-slate-600 animate-fade-in-up" style={{ animationDelay: '0.3s' }}>
            This is a dummy frontend to test the working of the chatbot.
          </p>
          <p className="text-lg text-slate-500 mt-4 animate-fade-in-up" style={{ animationDelay: '0.6s' }}>
            P.S. This is an official chatbot with knowledge of Adex.
          </p>
        </div>
      </div>

      {/* Chat bubble trigger */}
      <div className="fixed bottom-6 right-6 z-50">
        <Button
          onClick={() => setIsOpen(true)}
          className={`w-16 h-16 rounded-full bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 shadow-2xl border-0 transition-all duration-300 hover:scale-110 ${
            isOpen ? 'scale-0 opacity-0' : 'scale-100 opacity-100'
          }`}
        >
          <MessageSquare className="w-6 h-6 text-white" />
        </Button>
      </div>

      {/* Chat window */}
      <div className={`fixed bottom-6 right-6 w-[28rem] h-[40rem] bg-white/95 backdrop-blur-xl rounded-2xl shadow-2xl border border-white/20 z-50 transition-all duration-300 ${
        isOpen ? 'scale-100 opacity-100' : 'scale-95 opacity-0 pointer-events-none'
      }`}>
        {/* Chat header */}
        <div className="flex items-center justify-between p-4 border-b border-slate-200/50">
          <div className="flex items-center space-x-3">
            <div className="w-3 h-3 bg-green-400 rounded-full animate-pulse"></div>
            <h3 className="font-medium text-slate-800">Adex Intelligence</h3>
          </div>
          <Button
            variant="ghost"
            size="sm"
            onClick={() => setIsOpen(false)}
            className="w-8 h-8 p-0 hover:bg-slate-100 rounded-full"
          >
            <X className="w-4 h-4" />
          </Button>
        </div>

        {/* Messages area */}
        <ScrollArea className="h-[28rem] p-4">
          <div className="space-y-6">
            {messages.length === 0 && (
              <div className="text-center text-slate-500 mt-8">
                <MessageSquare className="w-12 h-12 mx-auto mb-3 opacity-30" />
                <p>Start a conversation...</p>
              </div>
            )}
            
            {messages.map((message, index) => (
              <div
                key={index}
                className={`flex items-start gap-3 ${
                  message.role === 'user' ? 'flex-row-reverse' : ''
                } animate-fade-in`}
              >
                <div
                  className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
                    message.role === 'user' ? 'bg-slate-700' : 'bg-slate-200'
                  }`}
                >
                  {message.role === 'user' ? (
                    <User className="w-5 h-5 text-white" />
                  ) : (
                    <Bot className="w-5 h-5 text-slate-600" />
                  )}
                </div>
                <div
                  className={`max-w-[80%] px-4 py-3 rounded-2xl ${
                    message.role === 'user'
                      ? 'bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-br-none'
                      : 'bg-white border text-slate-800 rounded-bl-none'
                  }`}
                >
                  <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
                </div>
              </div>
            ))}
            
            {isLoading && (
              <div className="flex items-start gap-3 animate-fade-in">
                <div className="w-8 h-8 rounded-full bg-slate-200 flex items-center justify-center flex-shrink-0">
                  <Bot className="w-5 h-5 text-slate-600" />
                </div>
                <div className="bg-white border text-slate-800 px-4 py-3 rounded-2xl rounded-bl-none">
                  <div className="flex items-center space-x-1.5">
                    <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce"></div>
                    <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                    <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
        </ScrollArea>

        {/* Input area */}
        <div className="p-4 border-t border-slate-200/50">
          <div className="flex space-x-2">
            <Input
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Ask anything about us and our services"
              className="flex-1 bg-slate-50 border-slate-200 focus:border-blue-400 focus:ring-blue-400/20 rounded-full px-4"
              disabled={isLoading}
            />
            {browserSupportsSpeechRecognition && (
              <Button
                type="button"
                onClick={handleListen}
                disabled={isLoading}
                className={`w-10 h-10 p-0 rounded-full shrink-0 transition-colors ${
                  listening ? 'bg-red-500 hover:bg-red-600 text-white' : 'bg-slate-200 hover:bg-slate-300'
                }`}
              >
                <Mic className="w-4 h-4" />
              </Button>
            )}
            <Button
              onClick={sendMessage}
              disabled={!inputValue.trim() || isLoading}
              className="w-10 h-10 p-0 rounded-full bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 disabled:opacity-50"
            >
              <Send className="w-4 h-4" />
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Index;
