Pages:
	Home
		The page has five sections:
			Header/navbar
			cv-section - with my resume
			projects-section - this section include my last tree projects (by updated_date)
			posts-section - include my last six posts
			footer
	Blog
		under header has sorting elements
		posts are showing by three columns in row
	Portfolio
		under header has sorting elements
		project are showing by big, single card in row
	Contacts
		include static text with links/addresses to my email/social networks
Subpages:
	Blog --> Single Blog Page
	Blog --> CRED new post
	Portfolio --> Single Project Page
	Portfolio--> CRED new post
Models:
	Tag:
		name = models.CharField(max_length=100, unique=True)
		
		def __str__(self):
			return self.name
	Post:
		title = models.CharField(max_length=100)
		short_desc = models.CharField(max_length=200)
		image = models.ImageField(upload_to='posts/%Y/%m/%d/')
		content = models.TextField()
		slug = models.SlugField() -> this field response for single post page link and for field creation I will be use slugify? function with self.title attr
		likes = models.IntegerField()
		tags = models.ManyToManyField(Tag)
		created_date = models.DateField(auto_add_now=True)
	Project:
		title = models.CharField(max_length=100)
		short_desc = models.CharField(max_length=200)
		image = models.ImageField(upload_to='projects/%Y/%m/%d/')
		content = models.TextField()
		slug = models.SlugField() -> this field response for single project page link and for field creation I will be use slugify? function with self.title attr
		likes = models.IntegerField()
		created_date = models.DateField(auto_now_add=True)
		updated_date = models.DateTimeField(auto_now=True)
	Project/Post Image:
		if I want to use several images for posts or project I need to create this class and change image field
		from models.ImageField to models.ManyToManyField for Post/Project class
		image = models.ImageField(upload_to={base_folder}/%Y/%m/%d/)