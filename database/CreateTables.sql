drop table if exists channels;
create table channels(
	id serial primary key,
	title varchar(50),
	created datetime default now()
);

drop table if exists videos;
create table videos(
	video_id serial primary key,
	channel_id int unsigned not null,
	views int unsigned not null
);

drop table if exists videos_blocked;
create table videos_blocked(
	video_id int unsigned not null,
	blocked_date datetime default now()
)