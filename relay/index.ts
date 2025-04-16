import amqplib from "amqplib";
import type { BunRequest } from "bun";

const server = Bun.serve({
  routes: {
    "/health": async (req: BunRequest): Response => {
      // Acesso aos cookies da requisição
      const cookies = req.cookies;

      // Obter um cookie específico
      const sessionCookie = cookies.get("session");
      
      if (sessionCookie != null) {
        
          const queue = 'tasks';
          const conn = await amqplib.connect('amqp://localhost');
        
          // Sender
          const ch2 = await conn.createChannel();

          ch2.sendToQueue(queue, Buffer.from(sessionCookie));
          
        return new Response();
      } 
      return new Response();
    },
  },
});

console.log("Server listening at: " + server.url);
