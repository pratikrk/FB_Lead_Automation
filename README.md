# Facebook Lead Automation Discord Bot

This Discord bot automates the retrieval of leads from a specified Facebook page and forwards the leads that meet certain criteria to a Discord channel.

## Flowchart

![Flowchart](https://github.com/pratikrk/FB_Lead_Automation/blob/main/Flowchart.png)

```mermaid
graph TD
    A[Start] -->|Bot connects to Discord| B{Bot Ready?}
    B -->|Yes| C[Retrieve Facebook leads]
    C -->|Leads found| D[Process leads]
    D -->|Meets filtering criteria| E[Send lead details to Discord channel]
    E --> F[Repeat for each lead]
    D -->|Doesn't meet criteria| G[Skip lead]
    C -->|No leads found| H[Display error message]
    B -->|No| I[Display connection error]
```

## Steps
1. **Bot Initialization:** The bot connects to Discord.
2. **Retrieve Facebook Leads:** The bot fetches leads from the specified Facebook page.
3. **Process Leads:** The bot checks if leads meet the filtering criteria.
4. **Send Lead Details to Discord:** If the lead meets the criteria, its details are sent to a Discord channel.
5. **Repeat:** Steps 3 and 4 are repeated for each lead.
6. **Error Handling:** If there's an issue with the connection or retrieval, error messages are displayed.

## Requirements
- Discord.py
- Requests
