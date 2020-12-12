
from bot.locals import Local

LOCAL = Local({
    'WRONG_ROOM' : 'I a\'m Not A Suppose To Be Here.\nID : <code>{CHAT_ID}</code>',
    'WELCOME_MESSAGE' : "Hi \nI Am Torrent Leecher",
    'PASS_REQUIRED' : '\n\nUse <code>/{cmd_pass} </code>to enter the password.',
    'LEECH_LIST_MESSAGE_HEADER' : '<b>Leech Status</b>',
    'LEECH_LIST_FORMAT' : 'Name: <code>{name}</code>\nStatus: {status}\nID: <code>{gid}</code>\n\n',
    'ARIA2_CHECKING_LINK' : "Checking...",
    'ARIA2_DOWNLOAD_STATUS' : "Downloading : <code>{name}</code>\n{block} {percentage}\nSize : {total_size}\nDN : {download_speed} / UP : {upload_speed}\nSeeder : {seeder}\nETA : {eta}\nID : <code>{gid}</code>",
    'ARIA2_DOWNLOAD_SUCCESS' : 'File Downloaded : <code>{name}</code>',
    'ARIA2_DOWNLOAD_CANCELED' : 'Download Canceled : <code>{name}</code>',
    'ARIA2_DEAD_LINK' : 'Download Auto Canceled : <code>{name}</code>\nYour Torrent/Link is Dead.',
    'ARIA2_NO_URI' : 'Link is invalid.',
    'UPLOADING_FILE' : 'Uploading : <code>{name}</code>',
    'UPLOADING_PROGRESS' : 'Uploading : <code>{name}</code>\n{block} {percentage}%\nSize : {size}\nUP : {upload_speed}/s\nETA : {eta}',
    'UPLOAD_FAILED_FILE_MISSING' : 'Upload : Failed. file Not Found.\n<code>{name}</code>',
    'GENERATE_THUMBNAIL' : 'Thumbnail : Generating.\n<code>{name}</code>',
    'SPLIT_FILE' : 'Spliting : <code>{name}</code>',
    'SPLIT_FAILED' : 'Split : Failed.\n<code>{name}</code>',
    'THUMBNAIL_NO_PHOTO' : 'Set <code>/{cmd_set_thumbnail}</code> as your photo caption.',
    'THUMBNAIL_DOWNLOADING' : 'Downloading Thumbnail.',
    'THUMBNAIL_DOWNLOADED' : 'Thumbnail download.',
    'THUMBNAIL_APPLIED' : 'Thumbnail Applied.',
    'THUMBNAIL_DELETING' : 'Deleting Thumbnail.',
    'THUMBNAIL_RESET' : 'Thumbnail Reset.',
    'UPLOAD_AS_DOC' : 'Upload As Document Set To {status}.',
    'UPLOAD_AS_ZIP' : 'Upload As ZIP File Set To {status}.',
    'TRACKER_RESET' : 'Default Torrent Tracker Reset.',
    'TRACKER_APPLIED' : 'Default Torrent Tracker Applied.',
    'HELP_MESSAGE_HEADER' : '<b>Bot Command</b>',
    'NO_HELP_INFO' : 'No Information',
    'COMMAND_START' : 'Start Bot',
    'COMMAND_PASSWORD' : 'enter password that required',
    'COMMAND_HELP' : 'This Message',
    'COMMAND_LEECH' : 'Leech Link Or Magnet',
    'COMMAND_CANCEL_LEECH' : 'Cancel Leeching',
    'COMMAND_LEECH_LIST' : 'List On Going Leech',
    'COMMAND_SET_THUMBNAIL' : 'Set Custom Video Thumbail',
    'COMMAND_RESET_THUMBNAIL' : 'Reset Custom Video Thumbnail',
    'COMMAND_UPLOAD_AS_DOC' : 'Toggle Upload Anything As Document',
    'COMMAND_UPLOAD_AS_ZIP' : 'Toggle Upload Anything As Bundled Zipfile',
    'COMMAND_SET_TRACKER' : 'Set Default Tracker, Sparated By Newline',
    'BLOCK_EMPTY' : "▱",
    "BLOCK_FILLED" : "▰"
})
