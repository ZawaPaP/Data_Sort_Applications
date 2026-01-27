import logging

class SetLogger():
    verbose = 0
    log = False
    
    def set_logger(self, name):
        logger = logging.getLogger(name)
        self.set_verbose(logger)
        f = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        if self.log:
            fh = logging.FileHandler("./log.log")
        else:
            fh = logging.StreamHandler()
        fh.setFormatter(f)
        logger.addHandler(fh)
        return logger
            
    def set_verbose(self, logger):
        if self.verbose and self.verbose >= 1:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.ERROR)
