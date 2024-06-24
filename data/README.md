# Data


```
Field	        Type	Description
publisher_id	uint16_t	                    The publisher ID assigned by Databento, which denotes the dataset and venue.
instrument_id	uint32_t	                    The numeric instrument ID.
ts_event	    uint64_t	                    The matching-engine-received timestamp expressed as the number of nanoseconds since the UNIX epoch.
price	        int64_t	                    The order price where every 1 unit corresponds to 1e-9, i.e. 1/1,000,000,000 or 0.000000001.
size	        uint32_t	                    The order quantity.
action	        char	                    The event action. Always Trade in the TBBO schema. See Action.
side	        char	                    The side that initiates the event. Can be Ask for a sell aggressor, Bid for a buy aggressor, or None where no side is specified by the original trade.
flags	        uint8_t	                    A bit field indicating event end, message characteristics, and data quality. See Flags.
depth	        uint8_t	T                   he book level where the update event occurred.
ts_recv	        uint64_t	                    The capture-server-received timestamp expressed as the number of nanoseconds since the UNIX epoch.
ts_in_delta	    int32_t	                    The matching-engine-sending timestamp expressed as the number of nanoseconds before ts_recv.
sequence	    uint32_t	                    The message sequence number assigned at the venue.
bid_px_00	    int64_t	                    The bid price at the top level.
ask_px_00	        int64_t	                    The ask price at the top level.
bid_sz_00	        uint32_t	                    The bid size at the top level.
ask_sz_00	        uint32_t	                    The ask size at the top level.
bid_ct_00	        uint32_t	                    The number of bid orders at the top level.
ask_ct_00	        uint32_t	                    The number of ask orders at the top level.
```