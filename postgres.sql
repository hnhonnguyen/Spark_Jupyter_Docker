DROP TABLE IF EXISTS public.user_rating;
CREATE TABLE IF NOT EXISTS public.user_rating
(
    case_id SERIAL,
    user_id bigint,
    comment varchar(512),
    case_created_at timestamp,
    case_rating smallint NOT NULL,
    case_category_1 varchar(256),
    case_category_2 varchar(256),
    CONSTRAINT user_rating_pkey PRIMARY KEY (case_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_rating
    OWNER to "postgresUser";


INSERT INTO public.user_rating(
	user_id, comment, case_created_at, case_rating, case_category_1, case_category_2)
	VALUES (56,'Nước ngon lắm','2020-03-01 20:34:00',5,'Product','Drink'),
(67,'Máy lạnh nóng quá','2020-03-04 20:34:00',1,'Facility','Air Conditioner'),
(78,'Bạn thu ngân rất dễ thương','2020-03-05 20:34:00',3,'Service','Cashier'),
(78,'Hôm nay bánh mì mình ăn bị chua','2020-03-02 08:34:00',2,'Product','Food')
	;