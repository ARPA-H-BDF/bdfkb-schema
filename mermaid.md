```mermaid
erDiagram
Common-Tool {
    string tool_id  
    string title  
    string desc  
}
LLMTool {
    LLM-TypeList llm_offered  
    string tool_id  
    string title  
    string desc  
}
CustomExtendedToolClass {
    string nickname  
    string custom_metric_1  
    number custom_metric_2  
    LLM-TypeList llm_offered  
    string tool_id  
    string title  
    string desc  
}

LLMTool ||--|o Common-Tool : "connection"
CustomExtendedToolClass ||--|o LLMTool : "connection-2"
CustomExtendedToolClass ||--|o Common-Tool : "connection"

```

