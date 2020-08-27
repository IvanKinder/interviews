select id, title, sum(views) from
channels left join videos on id = channel_id
where video_id not in (select video_id from videos_blocked)
and (day(now()) - day(created)) < 90
group by id

