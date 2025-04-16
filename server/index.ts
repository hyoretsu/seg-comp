import amqplib from "amqplib";

const server = Bun.serve({
  routes: {
    "/health": (req: Request): Response => {
      // Acesso aos cookies da requisição
      const cookies = req.cookies;

      // Obter um cookie específico
      const sessionCookie = cookies.get("session");
      if (sessionCookie != null) {
        (async () => {
          const queue = 'tasks';
          const conn = await amqplib.connect('amqp://localhost');
        
          const ch1 = await conn.createChannel();
          await ch1.assertQueue(queue);
          
          // Listener
          ch1.consume(queue, (cookies) => {
            if (cookies !== null) {
              console.log('Received:', cookies.content.toString());
              ch1.ack(cookies);
            } else {
              console.log('Consumer cancelled by server');
            }
          });

        })();
        return new Response();
      } 
      return new Response();
    },
  },
});

console.log("Server listening at: " + server.url);


// import { sql, serve } from "bun";

// serve({
//   port: 3001,
//   routes: {
//     "/api/version": async () => {
//       const [version] = await sql`SELECT version()`;
//       return Response.json(version);
//     },amqp://
//   },
// });
