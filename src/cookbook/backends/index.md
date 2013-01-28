# Deploying Backends #

[TOC]

## Introduction ##

OpenChange server implements a Storage Abstraction Layer (SAL)
middleware called MAPIStore, providing an API for remote system to
interface with OpenChange and OpenChange to push and pull information
(messages, folders) within these systems.

<br/>
## Available Backends ##
<br/>

Backends | Type     | Setup Guide
---------|----------|-------------
  SOGo   | Multiple | [SOGo Backend Setup](sogo/index.html)

<br/>
## Backend Feature Matrix ##
<br/>

Backends | Mail   | Calendaring   | Contacts   | Task    |   Notes  | Cached mode support   | Setup Guide
-------- | :----: | :-----------: | :--------: | :-----: | :------: | :-------------------: | :-----------
  SOGo   | yes    |    yes        |   yes      |  yes    |   yes    |        yes            | [SOGo Backend Setup](sogo/index.html)

