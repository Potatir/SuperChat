PGDMP         1                {         	   superchat    15.4    15.4 u    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    49498 	   superchat    DATABASE     }   CREATE DATABASE superchat WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE superchat;
                postgres    false            �            1259    49518    allip    TABLE     i   CREATE TABLE public.allip (
    ipid integer NOT NULL,
    ipadress text NOT NULL,
    userid integer
);
    DROP TABLE public.allip;
       public         heap    postgres    false            �            1259    49517    allip_ipid_seq    SEQUENCE     �   CREATE SEQUENCE public.allip_ipid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.allip_ipid_seq;
       public          postgres    false    219            �           0    0    allip_ipid_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.allip_ipid_seq OWNED BY public.allip.ipid;
          public          postgres    false    218            �            1259    49572    bfriends    TABLE     z   CREATE TABLE public.bfriends (
    bfriendid integer NOT NULL,
    username text NOT NULL,
    userid integer NOT NULL
);
    DROP TABLE public.bfriends;
       public         heap    postgres    false            �            1259    49571    bfriends_bfriendid_seq    SEQUENCE     �   CREATE SEQUENCE public.bfriends_bfriendid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.bfriends_bfriendid_seq;
       public          postgres    false    227            �           0    0    bfriends_bfriendid_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.bfriends_bfriendid_seq OWNED BY public.bfriends.bfriendid;
          public          postgres    false    226            �            1259    49585 	   blacklist    TABLE     �   CREATE TABLE public.blacklist (
    baduserid integer NOT NULL,
    cause text,
    time_of_ban time without time zone NOT NULL,
    banuserpk integer NOT NULL
);
    DROP TABLE public.blacklist;
       public         heap    postgres    false            �            1259    49667    bot    TABLE     �   CREATE TABLE public.bot (
    botid integer NOT NULL,
    botname text NOT NULL,
    botfunc text NOT NULL,
    sp_chatid integer NOT NULL
);
    DROP TABLE public.bot;
       public         heap    postgres    false            �            1259    49666    bot_botid_seq    SEQUENCE     �   CREATE SEQUENCE public.bot_botid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.bot_botid_seq;
       public          postgres    false    240            �           0    0    bot_botid_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.bot_botid_seq OWNED BY public.bot.botid;
          public          postgres    false    239            �            1259    49610    channel    TABLE     o   CREATE TABLE public.channel (
    channelid integer NOT NULL,
    channelname text NOT NULL,
    descr text
);
    DROP TABLE public.channel;
       public         heap    postgres    false            �            1259    49609    channel_channelid_seq    SEQUENCE     �   CREATE SEQUENCE public.channel_channelid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.channel_channelid_seq;
       public          postgres    false    232            �           0    0    channel_channelid_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.channel_channelid_seq OWNED BY public.channel.channelid;
          public          postgres    false    231            �            1259    49619    channel_users    TABLE     �   CREATE TABLE public.channel_users (
    userid integer NOT NULL,
    channelid integer NOT NULL,
    channeluserpk integer NOT NULL
);
 !   DROP TABLE public.channel_users;
       public         heap    postgres    false            �            1259    49636    channel_users_admin    TABLE     �   CREATE TABLE public.channel_users_admin (
    adminpk integer NOT NULL,
    adminuserid integer NOT NULL,
    channelid integer NOT NULL
);
 '   DROP TABLE public.channel_users_admin;
       public         heap    postgres    false            �            1259    49635    channel_users_admin_adminpk_seq    SEQUENCE     �   CREATE SEQUENCE public.channel_users_admin_adminpk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.channel_users_admin_adminpk_seq;
       public          postgres    false    236            �           0    0    channel_users_admin_adminpk_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.channel_users_admin_adminpk_seq OWNED BY public.channel_users_admin.adminpk;
          public          postgres    false    235            �            1259    49618    channel_users_channeluserpk_seq    SEQUENCE     �   CREATE SEQUENCE public.channel_users_channeluserpk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.channel_users_channeluserpk_seq;
       public          postgres    false    234            �           0    0    channel_users_channeluserpk_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.channel_users_channeluserpk_seq OWNED BY public.channel_users.channeluserpk;
          public          postgres    false    233            �            1259    49509    email    TABLE     �   CREATE TABLE public.email (
    emailid integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    email text NOT NULL
);
    DROP TABLE public.email;
       public         heap    postgres    false            �            1259    49508    email_emailid_seq    SEQUENCE     �   CREATE SEQUENCE public.email_emailid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.email_emailid_seq;
       public          postgres    false    217            �           0    0    email_emailid_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.email_emailid_seq OWNED BY public.email.emailid;
          public          postgres    false    216            �            1259    49546    groups    TABLE     j   CREATE TABLE public.groups (
    groupid integer NOT NULL,
    groupname text NOT NULL,
    descr text
);
    DROP TABLE public.groups;
       public         heap    postgres    false            �            1259    49545    groups_groupid_seq    SEQUENCE     �   CREATE SEQUENCE public.groups_groupid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.groups_groupid_seq;
       public          postgres    false    223            �           0    0    groups_groupid_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.groups_groupid_seq OWNED BY public.groups.groupid;
          public          postgres    false    222            �            1259    49555 
   groupusers    TABLE     �   CREATE TABLE public.groupusers (
    userid integer NOT NULL,
    groupid integer NOT NULL,
    groupuserpk integer NOT NULL
);
    DROP TABLE public.groupusers;
       public         heap    postgres    false            �            1259    49554    groupusers_groupuserpk_seq    SEQUENCE     �   CREATE SEQUENCE public.groupusers_groupuserpk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.groupusers_groupuserpk_seq;
       public          postgres    false    225            �           0    0    groupusers_groupuserpk_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.groupusers_groupuserpk_seq OWNED BY public.groupusers.groupuserpk;
          public          postgres    false    224            �            1259    49596    logs    TABLE     l   CREATE TABLE public.logs (
    logid integer NOT NULL,
    logfilename text,
    userid integer NOT NULL
);
    DROP TABLE public.logs;
       public         heap    postgres    false            �            1259    49595    logs_logid_seq    SEQUENCE     �   CREATE SEQUENCE public.logs_logid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.logs_logid_seq;
       public          postgres    false    230            �           0    0    logs_logid_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.logs_logid_seq OWNED BY public.logs.logid;
          public          postgres    false    229            �            1259    49532    messagehash    TABLE     �   CREATE TABLE public.messagehash (
    fileid integer NOT NULL,
    ownerid integer NOT NULL,
    filename text NOT NULL,
    falepath text NOT NULL
);
    DROP TABLE public.messagehash;
       public         heap    postgres    false            �            1259    49531    messagehash_fileid_seq    SEQUENCE     �   CREATE SEQUENCE public.messagehash_fileid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.messagehash_fileid_seq;
       public          postgres    false    221            �           0    0    messagehash_fileid_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.messagehash_fileid_seq OWNED BY public.messagehash.fileid;
          public          postgres    false    220            �            1259    49681    messages    TABLE     �   CREATE TABLE public.messages (
    mess_id integer NOT NULL,
    from_username text,
    mess_text text,
    to_username text
);
    DROP TABLE public.messages;
       public         heap    postgres    false            �            1259    49680    messages_mess_id_seq    SEQUENCE     �   CREATE SEQUENCE public.messages_mess_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.messages_mess_id_seq;
       public          postgres    false    242            �           0    0    messages_mess_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.messages_mess_id_seq OWNED BY public.messages.mess_id;
          public          postgres    false    241            �            1259    49653    sp_chat    TABLE     p   CREATE TABLE public.sp_chat (
    sp_chatid integer NOT NULL,
    chatname text,
    userid integer NOT NULL
);
    DROP TABLE public.sp_chat;
       public         heap    postgres    false            �            1259    49652    sp_chat_sp_chatid_seq    SEQUENCE     �   CREATE SEQUENCE public.sp_chat_sp_chatid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.sp_chat_sp_chatid_seq;
       public          postgres    false    238            �           0    0    sp_chat_sp_chatid_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.sp_chat_sp_chatid_seq OWNED BY public.sp_chat.sp_chatid;
          public          postgres    false    237            �            1259    49500    users    TABLE     s   CREATE TABLE public.users (
    userid integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    49499    users_userid_seq    SEQUENCE     �   CREATE SEQUENCE public.users_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.users_userid_seq;
       public          postgres    false    215            �           0    0    users_userid_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.users_userid_seq OWNED BY public.users.userid;
          public          postgres    false    214            �           2604    49521 
   allip ipid    DEFAULT     h   ALTER TABLE ONLY public.allip ALTER COLUMN ipid SET DEFAULT nextval('public.allip_ipid_seq'::regclass);
 9   ALTER TABLE public.allip ALTER COLUMN ipid DROP DEFAULT;
       public          postgres    false    219    218    219            �           2604    49575    bfriends bfriendid    DEFAULT     x   ALTER TABLE ONLY public.bfriends ALTER COLUMN bfriendid SET DEFAULT nextval('public.bfriends_bfriendid_seq'::regclass);
 A   ALTER TABLE public.bfriends ALTER COLUMN bfriendid DROP DEFAULT;
       public          postgres    false    226    227    227            �           2604    49670 	   bot botid    DEFAULT     f   ALTER TABLE ONLY public.bot ALTER COLUMN botid SET DEFAULT nextval('public.bot_botid_seq'::regclass);
 8   ALTER TABLE public.bot ALTER COLUMN botid DROP DEFAULT;
       public          postgres    false    239    240    240            �           2604    49613    channel channelid    DEFAULT     v   ALTER TABLE ONLY public.channel ALTER COLUMN channelid SET DEFAULT nextval('public.channel_channelid_seq'::regclass);
 @   ALTER TABLE public.channel ALTER COLUMN channelid DROP DEFAULT;
       public          postgres    false    232    231    232            �           2604    49622    channel_users channeluserpk    DEFAULT     �   ALTER TABLE ONLY public.channel_users ALTER COLUMN channeluserpk SET DEFAULT nextval('public.channel_users_channeluserpk_seq'::regclass);
 J   ALTER TABLE public.channel_users ALTER COLUMN channeluserpk DROP DEFAULT;
       public          postgres    false    234    233    234            �           2604    49639    channel_users_admin adminpk    DEFAULT     �   ALTER TABLE ONLY public.channel_users_admin ALTER COLUMN adminpk SET DEFAULT nextval('public.channel_users_admin_adminpk_seq'::regclass);
 J   ALTER TABLE public.channel_users_admin ALTER COLUMN adminpk DROP DEFAULT;
       public          postgres    false    236    235    236            �           2604    49512    email emailid    DEFAULT     n   ALTER TABLE ONLY public.email ALTER COLUMN emailid SET DEFAULT nextval('public.email_emailid_seq'::regclass);
 <   ALTER TABLE public.email ALTER COLUMN emailid DROP DEFAULT;
       public          postgres    false    216    217    217            �           2604    49549    groups groupid    DEFAULT     p   ALTER TABLE ONLY public.groups ALTER COLUMN groupid SET DEFAULT nextval('public.groups_groupid_seq'::regclass);
 =   ALTER TABLE public.groups ALTER COLUMN groupid DROP DEFAULT;
       public          postgres    false    222    223    223            �           2604    49558    groupusers groupuserpk    DEFAULT     �   ALTER TABLE ONLY public.groupusers ALTER COLUMN groupuserpk SET DEFAULT nextval('public.groupusers_groupuserpk_seq'::regclass);
 E   ALTER TABLE public.groupusers ALTER COLUMN groupuserpk DROP DEFAULT;
       public          postgres    false    224    225    225            �           2604    49599 
   logs logid    DEFAULT     h   ALTER TABLE ONLY public.logs ALTER COLUMN logid SET DEFAULT nextval('public.logs_logid_seq'::regclass);
 9   ALTER TABLE public.logs ALTER COLUMN logid DROP DEFAULT;
       public          postgres    false    229    230    230            �           2604    49535    messagehash fileid    DEFAULT     x   ALTER TABLE ONLY public.messagehash ALTER COLUMN fileid SET DEFAULT nextval('public.messagehash_fileid_seq'::regclass);
 A   ALTER TABLE public.messagehash ALTER COLUMN fileid DROP DEFAULT;
       public          postgres    false    221    220    221            �           2604    49684    messages mess_id    DEFAULT     t   ALTER TABLE ONLY public.messages ALTER COLUMN mess_id SET DEFAULT nextval('public.messages_mess_id_seq'::regclass);
 ?   ALTER TABLE public.messages ALTER COLUMN mess_id DROP DEFAULT;
       public          postgres    false    242    241    242            �           2604    49656    sp_chat sp_chatid    DEFAULT     v   ALTER TABLE ONLY public.sp_chat ALTER COLUMN sp_chatid SET DEFAULT nextval('public.sp_chat_sp_chatid_seq'::regclass);
 @   ALTER TABLE public.sp_chat ALTER COLUMN sp_chatid DROP DEFAULT;
       public          postgres    false    238    237    238            �           2604    49503    users userid    DEFAULT     l   ALTER TABLE ONLY public.users ALTER COLUMN userid SET DEFAULT nextval('public.users_userid_seq'::regclass);
 ;   ALTER TABLE public.users ALTER COLUMN userid DROP DEFAULT;
       public          postgres    false    214    215    215            t          0    49518    allip 
   TABLE DATA           7   COPY public.allip (ipid, ipadress, userid) FROM stdin;
    public          postgres    false    219   n�       |          0    49572    bfriends 
   TABLE DATA           ?   COPY public.bfriends (bfriendid, username, userid) FROM stdin;
    public          postgres    false    227   ��       }          0    49585 	   blacklist 
   TABLE DATA           M   COPY public.blacklist (baduserid, cause, time_of_ban, banuserpk) FROM stdin;
    public          postgres    false    228   ��       �          0    49667    bot 
   TABLE DATA           A   COPY public.bot (botid, botname, botfunc, sp_chatid) FROM stdin;
    public          postgres    false    240   ł       �          0    49610    channel 
   TABLE DATA           @   COPY public.channel (channelid, channelname, descr) FROM stdin;
    public          postgres    false    232   �       �          0    49619    channel_users 
   TABLE DATA           I   COPY public.channel_users (userid, channelid, channeluserpk) FROM stdin;
    public          postgres    false    234   ��       �          0    49636    channel_users_admin 
   TABLE DATA           N   COPY public.channel_users_admin (adminpk, adminuserid, channelid) FROM stdin;
    public          postgres    false    236   �       r          0    49509    email 
   TABLE DATA           C   COPY public.email (emailid, username, password, email) FROM stdin;
    public          postgres    false    217   9�       x          0    49546    groups 
   TABLE DATA           ;   COPY public.groups (groupid, groupname, descr) FROM stdin;
    public          postgres    false    223   V�       z          0    49555 
   groupusers 
   TABLE DATA           B   COPY public.groupusers (userid, groupid, groupuserpk) FROM stdin;
    public          postgres    false    225   s�                 0    49596    logs 
   TABLE DATA           :   COPY public.logs (logid, logfilename, userid) FROM stdin;
    public          postgres    false    230   ��       v          0    49532    messagehash 
   TABLE DATA           J   COPY public.messagehash (fileid, ownerid, filename, falepath) FROM stdin;
    public          postgres    false    221   ��       �          0    49681    messages 
   TABLE DATA           R   COPY public.messages (mess_id, from_username, mess_text, to_username) FROM stdin;
    public          postgres    false    242   ʃ       �          0    49653    sp_chat 
   TABLE DATA           >   COPY public.sp_chat (sp_chatid, chatname, userid) FROM stdin;
    public          postgres    false    238   �       p          0    49500    users 
   TABLE DATA           ;   COPY public.users (userid, username, password) FROM stdin;
    public          postgres    false    215   �       �           0    0    allip_ipid_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.allip_ipid_seq', 1, false);
          public          postgres    false    218            �           0    0    bfriends_bfriendid_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.bfriends_bfriendid_seq', 1, false);
          public          postgres    false    226            �           0    0    bot_botid_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.bot_botid_seq', 1, false);
          public          postgres    false    239            �           0    0    channel_channelid_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.channel_channelid_seq', 1, false);
          public          postgres    false    231            �           0    0    channel_users_admin_adminpk_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.channel_users_admin_adminpk_seq', 1, false);
          public          postgres    false    235            �           0    0    channel_users_channeluserpk_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.channel_users_channeluserpk_seq', 1, false);
          public          postgres    false    233            �           0    0    email_emailid_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.email_emailid_seq', 1, false);
          public          postgres    false    216            �           0    0    groups_groupid_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.groups_groupid_seq', 1, false);
          public          postgres    false    222            �           0    0    groupusers_groupuserpk_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.groupusers_groupuserpk_seq', 1, false);
          public          postgres    false    224            �           0    0    logs_logid_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.logs_logid_seq', 1, false);
          public          postgres    false    229            �           0    0    messagehash_fileid_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.messagehash_fileid_seq', 1, false);
          public          postgres    false    220            �           0    0    messages_mess_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.messages_mess_id_seq', 1, false);
          public          postgres    false    241            �           0    0    sp_chat_sp_chatid_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.sp_chat_sp_chatid_seq', 1, false);
          public          postgres    false    237            �           0    0    users_userid_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.users_userid_seq', 1, false);
          public          postgres    false    214            �           2606    49525    allip allip_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.allip
    ADD CONSTRAINT allip_pkey PRIMARY KEY (ipid);
 :   ALTER TABLE ONLY public.allip DROP CONSTRAINT allip_pkey;
       public            postgres    false    219            �           2606    49579    bfriends bfriends_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.bfriends
    ADD CONSTRAINT bfriends_pkey PRIMARY KEY (bfriendid);
 @   ALTER TABLE ONLY public.bfriends DROP CONSTRAINT bfriends_pkey;
       public            postgres    false    227            �           2606    49674    bot bot_pkey 
   CONSTRAINT     M   ALTER TABLE ONLY public.bot
    ADD CONSTRAINT bot_pkey PRIMARY KEY (botid);
 6   ALTER TABLE ONLY public.bot DROP CONSTRAINT bot_pkey;
       public            postgres    false    240            �           2606    49617    channel channel_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.channel
    ADD CONSTRAINT channel_pkey PRIMARY KEY (channelid);
 >   ALTER TABLE ONLY public.channel DROP CONSTRAINT channel_pkey;
       public            postgres    false    232            �           2606    49641 ,   channel_users_admin channel_users_admin_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.channel_users_admin
    ADD CONSTRAINT channel_users_admin_pkey PRIMARY KEY (adminpk);
 V   ALTER TABLE ONLY public.channel_users_admin DROP CONSTRAINT channel_users_admin_pkey;
       public            postgres    false    236            �           2606    49624     channel_users channel_users_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.channel_users
    ADD CONSTRAINT channel_users_pkey PRIMARY KEY (channeluserpk);
 J   ALTER TABLE ONLY public.channel_users DROP CONSTRAINT channel_users_pkey;
       public            postgres    false    234            �           2606    49516    email email_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.email
    ADD CONSTRAINT email_pkey PRIMARY KEY (emailid);
 :   ALTER TABLE ONLY public.email DROP CONSTRAINT email_pkey;
       public            postgres    false    217            �           2606    49553    groups groups_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (groupid);
 <   ALTER TABLE ONLY public.groups DROP CONSTRAINT groups_pkey;
       public            postgres    false    223            �           2606    49560    groupusers groupusers_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.groupusers
    ADD CONSTRAINT groupusers_pkey PRIMARY KEY (groupuserpk);
 D   ALTER TABLE ONLY public.groupusers DROP CONSTRAINT groupusers_pkey;
       public            postgres    false    225            �           2606    49603    logs logs_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.logs
    ADD CONSTRAINT logs_pkey PRIMARY KEY (logid);
 8   ALTER TABLE ONLY public.logs DROP CONSTRAINT logs_pkey;
       public            postgres    false    230            �           2606    49539    messagehash messagehash_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.messagehash
    ADD CONSTRAINT messagehash_pkey PRIMARY KEY (fileid);
 F   ALTER TABLE ONLY public.messagehash DROP CONSTRAINT messagehash_pkey;
       public            postgres    false    221            �           2606    49688    messages messages_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (mess_id);
 @   ALTER TABLE ONLY public.messages DROP CONSTRAINT messages_pkey;
       public            postgres    false    242            �           2606    49660    sp_chat sp_chat_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.sp_chat
    ADD CONSTRAINT sp_chat_pkey PRIMARY KEY (sp_chatid);
 >   ALTER TABLE ONLY public.sp_chat DROP CONSTRAINT sp_chat_pkey;
       public            postgres    false    238            �           2606    49507    users users_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (userid);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    215            �           2606    49642 "   channel_users_admin adminuserid_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.channel_users_admin
    ADD CONSTRAINT adminuserid_fk FOREIGN KEY (adminuserid) REFERENCES public.users(userid) ON DELETE CASCADE;
 L   ALTER TABLE ONLY public.channel_users_admin DROP CONSTRAINT adminuserid_fk;
       public          postgres    false    236    3257    215            �           2606    49590    blacklist banuserpk_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.blacklist
    ADD CONSTRAINT banuserpk_fk FOREIGN KEY (banuserpk) REFERENCES public.users(userid) ON DELETE CASCADE;
 @   ALTER TABLE ONLY public.blacklist DROP CONSTRAINT banuserpk_fk;
       public          postgres    false    3257    228    215            �           2606    49630    channel_users channelid_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.channel_users
    ADD CONSTRAINT channelid_fk FOREIGN KEY (channelid) REFERENCES public.channel(channelid) ON DELETE CASCADE;
 D   ALTER TABLE ONLY public.channel_users DROP CONSTRAINT channelid_fk;
       public          postgres    false    3273    232    234            �           2606    49647     channel_users_admin channelid_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.channel_users_admin
    ADD CONSTRAINT channelid_fk FOREIGN KEY (channelid) REFERENCES public.channel(channelid) ON DELETE CASCADE;
 J   ALTER TABLE ONLY public.channel_users_admin DROP CONSTRAINT channelid_fk;
       public          postgres    false    3273    232    236            �           2606    49566    groupusers groupid_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.groupusers
    ADD CONSTRAINT groupid_fk FOREIGN KEY (groupid) REFERENCES public.groups(groupid) ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.groupusers DROP CONSTRAINT groupid_fk;
       public          postgres    false    223    225    3265            �           2606    49540    messagehash ownerid_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.messagehash
    ADD CONSTRAINT ownerid_fk FOREIGN KEY (ownerid) REFERENCES public.users(userid) ON DELETE CASCADE;
 @   ALTER TABLE ONLY public.messagehash DROP CONSTRAINT ownerid_fk;
       public          postgres    false    215    221    3257            �           2606    49675    bot sp_chatid_fk    FK CONSTRAINT     z   ALTER TABLE ONLY public.bot
    ADD CONSTRAINT sp_chatid_fk FOREIGN KEY (sp_chatid) REFERENCES public.sp_chat(sp_chatid);
 :   ALTER TABLE ONLY public.bot DROP CONSTRAINT sp_chatid_fk;
       public          postgres    false    240    3279    238            �           2606    49526    allip userid_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.allip
    ADD CONSTRAINT userid_fk FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE;
 9   ALTER TABLE ONLY public.allip DROP CONSTRAINT userid_fk;
       public          postgres    false    215    3257    219            �           2606    49561    groupusers userid_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.groupusers
    ADD CONSTRAINT userid_fk FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE;
 >   ALTER TABLE ONLY public.groupusers DROP CONSTRAINT userid_fk;
       public          postgres    false    3257    215    225            �           2606    49580    bfriends userid_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.bfriends
    ADD CONSTRAINT userid_fk FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE;
 <   ALTER TABLE ONLY public.bfriends DROP CONSTRAINT userid_fk;
       public          postgres    false    215    3257    227            �           2606    49604    logs userid_fk    FK CONSTRAINT     p   ALTER TABLE ONLY public.logs
    ADD CONSTRAINT userid_fk FOREIGN KEY (userid) REFERENCES public.users(userid);
 8   ALTER TABLE ONLY public.logs DROP CONSTRAINT userid_fk;
       public          postgres    false    215    230    3257            �           2606    49625    channel_users userid_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.channel_users
    ADD CONSTRAINT userid_fk FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE;
 A   ALTER TABLE ONLY public.channel_users DROP CONSTRAINT userid_fk;
       public          postgres    false    215    3257    234            �           2606    49661    sp_chat userid_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.sp_chat
    ADD CONSTRAINT userid_fk FOREIGN KEY (userid) REFERENCES public.users(userid) ON DELETE CASCADE;
 ;   ALTER TABLE ONLY public.sp_chat DROP CONSTRAINT userid_fk;
       public          postgres    false    215    3257    238            t      x������ � �      |      x������ � �      }      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      r      x������ � �      x      x������ � �      z      x������ � �            x������ � �      v      x������ � �      �      x������ � �      �      x������ � �      p      x������ � �     