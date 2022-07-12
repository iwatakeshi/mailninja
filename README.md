# NinjaMail

A minimal marketing, automation & email service. (WIP)


## Architecture

### Frontend

The frontend will be a Next.js app that will run in front of the API server. Mantine UI will be used as the UI framework.

**Authentication**

NextAuth will be used to authenticate the user. The user will login with username and password.


### Backend

The backend will be a Nest.js app. The glue between the frontend and the back is the reverse proxy that is provided by the build system (Nx). The database will be powered by Supabase and Prisma will be used as the ORM for the database.

**Authorization**

To use the API, you will need to provide an API key generated during the signup process or added manually to the database.

## Reading Materials

### Amazon SES

[Handling Bounces and Complaints](https://aws.amazon.com/blogs/messaging-and-targeting/handling-bounces-and-complaints/?pg=ln&p=ses&sec=bl)

[Warming up dedicated IP addresses](https://docs.aws.amazon.com/ses/latest/dg/dedicated-ip-warming.html)

### Dedicated IP

[Dedicated IP Address vs Shared IP Address (Debunking Myths)](https://kinsta.com/blog/dedicated-ip-address/#dedicated-ip-vs-shared-email)

### Deployment

[Gitalytics - A simple overview of Github activities](https://dev.to/shhdharmen/gitalytics-a-simple-overview-of-github-activities-ohd)

## Watching Materials

[Introduction to TCP/IP and Sockets, part 1: Introducing the protocols and API](https://www.youtube.com/watch?v=C7CpfL1p6y0)
