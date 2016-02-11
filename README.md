state format:
"{
	"rows": rows,
	"columns": columns,
	"nr_drones": nr_drones,
	"nr_turns": nr_turns,
	"max_paylod": max_paylod,
	"products": products,
	"warehouses": [{"id": id, "pos": (x, y), "items": [count]}],
	"orders": orders
}"
offer:
"{
	"order": order to be worked
	"product": product to be delivered
	"count": count of items
}"
