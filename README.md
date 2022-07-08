# MailNinja

A minimal marketing, automation & email service. (WIP)

## Architecture

While it's typically difficult to migrate to another stack after deploying an application into production. We plan to prototype and incrementally build the application as our knowledge grows during the development process. We do not recommend anyone to use this application in production until we stablize the stack and the API.

To begin with, we will use a simple Express backend and a React application on the frontend. Later on, we will split the two in order to scale the frontend and the backend individually. We may migrate the frontend to a Next.js application in the future.

**Authorization**

To use the API, you will need to provide an API key generated during the signup process or added manually to the database.

## Reading Material

### Amazon SES

[Handling Bounces and Complaints](https://aws.amazon.com/blogs/messaging-and-targeting/handling-bounces-and-complaints/?pg=ln&p=ses&sec=bl)

[Warming up dedicated IP addresses](https://docs.aws.amazon.com/ses/latest/dg/dedicated-ip-warming.html)
