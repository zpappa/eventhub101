from types import SimpleNamespace


Settings = SimpleNamespace(**{
            "eh": SimpleNamespace(**{
                        "hostname": "zeashan.servicebus.windows.net:9093",
                        "sas_policy": "default",
                        "sas_key": "0kN4cov0mxeNvBbLCXEe0pmObohjJc66gQTdaXme4D8=",
                        "event_hub_name": "dev",
                        "partition": "0"
                      })
})
