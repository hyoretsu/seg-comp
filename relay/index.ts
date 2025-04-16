import amqplib from 'amqplib'
import type { BunRequest } from 'bun'

const conn = await amqplib.connect(process.env.RABBITMQ_URL!)
const ch = await conn.createChannel()

const queue = 'default'
await ch.assertQueue(queue)

Bun.serve({
	port: process.env.PORT ?? 3333,
	routes: {
		'/health': async (req: BunRequest): Promise<Response> => {
			console.log('recebeu')
			const dataCookie = req.cookies.get('X-App-Data')
			if (dataCookie != null) {
				ch.sendToQueue(queue, Buffer.from(dataCookie))
			}

			return new Response()
		},
	},
})
