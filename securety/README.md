## AI agent Log Security Analyst

This agent is designed to act as a Log Security Analyst—it reads system logs and categorizes potential security threats.

## 1. Project Prerequisites

You will need to install the following libraries:
```bash
pip install langchain openai python-dotenv
```
##2. The Core Security Agent Code 

This script `log.py` sets up an agent with a "Security Persona" and a tool to "quarantine" suspicious IPs.

##  3. Key Architectural Concepts

Layer,Component,Security Goal
Observation,Log Scanners / SIEM,Feeding the agent real-time data from sources like ElasticSearch or AWS CloudWatch.
Reasoning,Prompt Engineering,Using frameworks like MITRE ATT&CK in the prompt to help the AI categorize the threat.
Action,Tool Integration,"Giving the agent ""Write"" access only to specific security functions (like blocking an IP) rather than general shell access."
